package main

import (
	"materiale_api/configs"
	"materiale_api/routes"

	"github.com/gofiber/fiber/v2"
)

func main() {
	app := fiber.New()

	//run database
	configs.ConnectDB()
	routes.MaterialeRoute(app)

	app.Listen(":9090")
}
