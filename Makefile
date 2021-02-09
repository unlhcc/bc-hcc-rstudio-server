# what
PROG = bc-hcc-rstudio-server

VERSION = $(shell ${GIT} describe --tags | ${SED} 's/-/_/g')

# needed programs to build or install
GIT = /usr/bin/git
SED = /bin/sed
TAR = /bin/tar
GZIP = /bin/gzip
RPMBUILD = /usr/bin/rpmbuild
MOCK = /usr/bin/mock

# mock variables
RESULTDIR ?= .artifacts
CACHEDIR ?= .cache
ARCH ?= epel-7-x86_64

all: srpm rpm clean

${PROG}-${VERSION}.tar.gz:
	${TAR} --transform "s/^\./${PROG}-${VERSION}/" \
	       --exclude=${PROG}.tar \
	       --exclude=${RESULTDIR} \
	       --exclude=${CACHEDIR} \
	       --exclude-vcs \
	       -cf ${PROG}.tar .
	${GZIP} -9 -f ${PROG}.tar

tar: ${PROG}-${VERSION}.tar.gz

srpm: tar
	${MOCK} -r ${ARCH} --buildsrpm --define='package_version ${VERSION}' --sources=${PROG}.tar.gz \
        --spec=packaging/ondemand-bc_hcc_rstudio_server.spec --resultdir=${RESULTDIR}

rpm: tar
	${MOCK} -r ${ARCH} --define='package_version ${VERSION}' --resultdir=${RESULTDIR} --rebuild ${RESULTDIR}/*.src.rpm

clean:
	-${RM} ${PROG}.tar.gz
