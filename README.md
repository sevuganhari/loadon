# Load ON

Load CPU / Mem of a WebServer

## Expected
* Port 80 must be available on the Host, else modify `nginx/Dockerfile`

## Steps

`git clone git@github.com:sevuganhari/loadon.git`

`cd loadon`

`docker-compose up --build`

### Check CPU Usage

http://localhost/cpu_usage

### Load CPU Cores to 100%

http://localhost/cpu?cores=##

`cores` - number of cores you want to load to 100%

---
**Note** : Each request to load CPU to 100% will load additional cores. Will not reset the previous CPU Cores which were loaded to 100% of stress level.

---

### Check Mem Usage

http://localhost/mem_usage

### Load Mem in MB

http://localhost/mem?use=##

`use` - memory capacity to be used in MB

---
**Note**: Each request to load Mem will reset the previous Mem usage. Will not add to existing Mem usage.

---