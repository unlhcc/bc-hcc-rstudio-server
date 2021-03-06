# Disable debuginfo as it causes issues with bundled gems that build libraries
%global debug_package %{nil}
%global repo_name bc-hcc-rstudio-server
%global app_name bc_hcc_rstudio_server
%{!?package_version: %define package_version %{major}.%{minor}.%{patch}}
%{!?package_release: %define package_release 1}
%{!?git_tag: %define git_tag v%{package_version}}
%define git_tag_minus_v %(echo %{git_tag} | sed -r 's/^v//')

Name:     ondemand-%{app_name}
Version:  %{package_version}
Release:  %{package_release}%{?dist}
Summary:  Batch Connect - HCC RStudio Server

Group:    System Environment/Daemons
License:  MIT
URL:      https://git.unl.edu/hcc/bc-hcc-rstudio-server
Source0:  bc-hcc-rstudio-server.tar.gz

Requires: ondemand

# Disable automatic dependencies as it causes issues with bundled gems and
# node.js packages used in the apps
AutoReqProv: no

%description
DESCRIPTION

%prep
%setup -q -n %{repo_name}-%{git_tag_minus_v}


%build


%install
%__mkdir_p %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name}
%__cp -a ./. %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name}/
echo v%{version} > %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name}/VERSION

%files
%defattr(-,root,root)
%{_localstatedir}/www/ood/apps/sys/%{app_name}
%{_localstatedir}/www/ood/apps/sys/%{app_name}/manifest.yml


%changelog
* Thu Aug 02 2018 Morgan Rodgers <mrodgers@osc.edu> 0.6.0-1
- Add R 3.5.0 as an option for RStudio Server (mrodgers@osc.edu)

* Wed Apr 18 2018 Jeremy Nicklas <jnicklas@osc.edu> 0.5.0-1
- Bump bc_osc_rstudio_server to 0.5.0 (jnicklas@osc.edu)

* Wed Mar 28 2018 Jeremy Nicklas <jnicklas@osc.edu> 0.4.0-1
- Bump bc_osc_rstudio_server to 0.4.0 (jnicklas@osc.edu)

* Tue Feb 13 2018 Trey Dockendorf <tdockendorf@osc.edu> 0.3.0-1
- new package built with tito

