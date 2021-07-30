# Batch Connect - HCC RStudio Server

[![pipeline status](https://git.unl.edu/hcc/bc-hcc-rstudio-server/badges/master/pipeline.svg)](https://git.unl.edu/hcc/bc-hcc-rstudio-server/-/commits/master)
[![GitHub License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

An interactive app designed for OSC OnDemand that launches an [RStudio Server]
within a SLURM batch job.

Based off of https://github.com/OSC/bc_osc_rstudio_server.

## Prerequisites

This Batch Connect app requires the following software be installed on the
**compute nodes** that the batch job is intended to run on (**NOT** the
OnDemand node):

- [Lmod] 6.0.1+ or any other `module restore` and `module load <modules>` based
  CLI used to load appropriate environments within the batch job before
  launching the RStudio Server.
- [Singularity] 2.4.2+
- A Singularity image similar to [rocker/rstudio]

[RStudio Server]: https://www.rstudio.com/products/rstudio-server/
[Singularity]: http://singularity.lbl.gov/
[Lmod]: https://www.tacc.utexas.edu/research-development/tacc-projects/lmod
[rocker/rstudio]: https://hub.docker.com/r/rocker/rstudio

## Build/Install

Gitlab CI will automatically build both CentOS 7 and 8 RPMs.
They can be installed directly via `yum` for testing.

For production, add to the per-cluster common repos and require via puppet.

## Contributing

1. Fork it ( https://git.unl.edu/hcc/bc-hcc-rstudio-server/-/forks/new )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## License

* Documentation, website content, and logo is licensed under
  [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
* Code is licensed under MIT (see LICENSE.txt)
* RStudio, Shiny and the RStudio logo are all registered trademarks of RStudio.
