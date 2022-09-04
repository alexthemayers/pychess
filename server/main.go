package main

import (
	"flag"
	"net/http"

	"github.com/gin-gonic/gin"
)

var sAddress string

func init() {
	flag.StringVar(&sAddress, "sAddress", "localhost", "URL to listen on")
}

func main() {
	flag.Parse()
	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "pong",
		})
	})
	r.Run() // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
