# Resource Budget

Target host: 8 vCPU / 16 GB RAM.

## Always-on budget

- proxy: 160 MB, 0.20 CPU
- portfolio-api: 256 MB, 0.40 CPU
- portfolio-web: 280 MB, 0.40 CPU
- showcase-streamlit: 700 MB, 0.80 CPU
- nlp-spam-api: 600 MB, 0.80 CPU
- postgres: 400 MB, 0.20 CPU
- brainsight: 900 MB, 1.00 CPU
- getaround: 900 MB, 1.00 CPU
- fraudstream: 1200 MB, 1.20 CPU

Approximate steady-state cap: 5.39 GB RAM with headroom for OS, disk cache, and burst workloads.
