# Build images with pack

```bash
pack build rromanotero/light_sensor:latest --path services/light_sensor --builder gcr.io/buildpacks/builder:v1

pack build rromanotero/motor:latest --path services/motor --builder gcr.io/buildpacks/builder:v1
```
