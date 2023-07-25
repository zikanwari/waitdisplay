const http = require('http');
const {InfluxDB, Point} = require('@influxdata/influxdb-client')

const token = process.env.token
const url = 'http://10.0.0.2:8086'

let org = `lp-cloud`
let bucket = `zikanwari`

const client = new InfluxDB({url, token})

queryClient = client.getQueryApi(org)

fluxQuery = `from(bucket: "zikanwari")
|> range(start: -60m)
|> filter(fn: (r) => r["_measurement"] == "congestion")
|> last()`

const server = http.createServer((req, res) => {
    console.log(req.url)
    res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'});

    queryClient.queryRows(fluxQuery, {
    next: (row, tableMeta) => {
        const tableObject = tableMeta.toObject(row)
        console.log(tableObject._value)
        res.write(String(tableObject._value))

        
    },
    error: (error) => {
        console.error('\nえららー', error)
        res.end()
    },
    complete: () => {
        res.end()
    },
    })
});

server.listen(3000, () => {
    console.log('Server running on port 3000');
  });