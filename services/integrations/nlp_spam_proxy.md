# NLP Spam Integration

The unified demo profile routes `spam.<domain>` traffic to the CPU-safe NLP spam API.

- Source service: `../nlp-spam-detector-api` using `Dockerfile.cpu`
- Runtime mode: `live-interactive`
- Health endpoint: `/healthz`
- Memory budget: `600m`
- CPU budget: `0.80`
