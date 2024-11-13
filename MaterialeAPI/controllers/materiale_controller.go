package controllers

import (
	"context"
	"materiale_api/configs"
	"materiale_api/models"
	"materiale_api/responses"
	"net/http"
	"time"

	"github.com/go-playground/validator/v10"
	"github.com/gofiber/fiber/v2"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
)

var materialeCollection *mongo.Collection = configs.GetCollection(configs.DB, "materiale")
var validate = validator.New()

func HelloWorld(c *fiber.Ctx) error {
	return c.Status(http.StatusCreated).JSON("message", "Hello World")
}

func SaveMaterial(c *fiber.Ctx) error {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	var material models.Material

	// Extrage și validează datele din request
	if err := c.BodyParser(&material); err != nil {
		return c.Status(http.StatusBadRequest).JSON(responses.MaterialeResponse{
			Status:  http.StatusBadRequest,
			Message: "error",
			Data:    &fiber.Map{"data": err.Error()},
		})
	}
	if validationErr := validate.Struct(&material); validationErr != nil {
		return c.Status(http.StatusBadRequest).JSON(responses.MaterialeResponse{
			Status:  http.StatusBadRequest,
			Message: "error",
			Data:    &fiber.Map{"data": validationErr.Error()},
		})
	}

	// Creează documentul minimal `Material` doar cu câmpurile `ID` și `IDDisciplina`
	newMaterial := models.Material{
		ID:           primitive.NewObjectID(),
		IDDisciplina: material.IDDisciplina,
	}

	// Salvează documentul în baza de date
	result, err := materialeCollection.InsertOne(ctx, newMaterial)
	if err != nil {
		return c.Status(http.StatusInternalServerError).JSON(responses.MaterialeResponse{
			Status:  http.StatusInternalServerError,
			Message: "error",
			Data:    &fiber.Map{"data": err.Error()},
		})
	}

	// Returnează răspunsul de succes
	return c.Status(http.StatusCreated).JSON(responses.MaterialeResponse{
		Status:  http.StatusCreated,
		Message: "success",
		Data:    &fiber.Map{"data": result.InsertedID},
	})
}

func GetMaterial(c *fiber.Ctx) error {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	// Extrage `ID`-ul materialului din parametrii URL-ului
	materialID := c.Params("id")
	objID, err := primitive.ObjectIDFromHex(materialID)
	if err != nil {
		return c.Status(http.StatusBadRequest).JSON(responses.MaterialeResponse{
			Status:  http.StatusBadRequest,
			Message: "error",
			Data:    &fiber.Map{"data": "ID invalid"},
		})
	}

	// Căutare document în colecția `materiale` după `ID`
	var material models.Material
	err = materialeCollection.FindOne(ctx, bson.M{"_id": objID}).Decode(&material)
	if err != nil {
		if err == mongo.ErrNoDocuments {
			return c.Status(http.StatusNotFound).JSON(responses.MaterialeResponse{
				Status:  http.StatusNotFound,
				Message: "error",
				Data:    &fiber.Map{"data": "Materialul nu a fost găsit"},
			})
		}
		return c.Status(http.StatusInternalServerError).JSON(responses.MaterialeResponse{
			Status:  http.StatusInternalServerError,
			Message: "error",
			Data:    &fiber.Map{"data": err.Error()},
		})
	}

	// Returnează documentul găsit
	return c.Status(http.StatusOK).JSON(responses.MaterialeResponse{
		Status:  http.StatusOK,
		Message: "success",
		Data:    &fiber.Map{"data": material},
	})
}
