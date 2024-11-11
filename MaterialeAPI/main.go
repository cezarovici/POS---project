package main

import (
	"materiale_api/configs"

	"github.com/gofiber/fiber/v2"
)

func main() {
	app := fiber.New()

	//run database
	configs.ConnectDB()

	app.Listen(":9090")
}
