package proxy

import (
	"net/http"
	"net/url"
	"github.com/ethereum/go-ethereum/log"
)

const serverAddr string = "http://localhost:1520"

var esc = url.QueryEscape

func InformWorkerUpdate(workerName string){
	sendReq("/worker_upd?worker_name="+esc(workerName))
}

func InformWorkerHashrate(workerName,hashrate string) {
	sendReq("/worker_upd?worker_name="+esc(workerName) + "&hashrate=" + esc(hashrate))
}

func sendReq(s string){
	_,err:=http.Get(serverAddr+s)
	if err != nil{log.Warn("Ext GET request failed! Extensions server may be down!\n"+err.Error())}
}