package routes

import (
	"materiale_api/controllers"

	"github.com/gofiber/fiber/v2"
)

func MaterialeRoute(app *fiber.App) {
	app.Post("/materiale", controllers.SaveMaterial)
	app.Get("/materiale/:id", controllers.GetMaterial)
	app.Get("/", controllers.HelloWorld)
}
