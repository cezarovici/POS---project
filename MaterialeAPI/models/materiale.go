package models

import (
	"time"

	"go.mongodb.org/mongo-driver/bson/primitive"
)

type TipProba int

const (
	ActivitateLaborator TipProba = iota
	Seminar
	Proiect
)

type ProbaEvaluare struct {
	TipProba TipProba `bson:"tipProba"` // Tipul probei: laborator, seminar sau proiect
	Pondere  float32  `bson:"pondere"`  // Ponderea probei în nota finală
	Grade    float32  `bson:"grade"`    // Nota obținută la această probă
}

type FisierPDF struct {
	ID            primitive.ObjectID `bson:"_id,omitempty"`   // ID-ul unic al fișierului
	NumeFisier    string             `bson:"numeFisier"`      // Numele fișierului PDF
	URL           string             `bson:"url"`             // URL-ul pentru descărcare/accesare
	Dimensiune    int64              `bson:"dimensiune"`      // Dimensiunea fișierului (în bytes)
	Autor         string             `bson:"autor,omitempty"` // Numele autorului fișierului
	DataIncarcare time.Time          `bson:"dataIncarcare"`   // Data încărcării fișierului
}

type Material struct {
	ID                 primitive.ObjectID `bson:"_id,omitempty"`                // ID-ul unic în MongoDB
	IDDisciplina       string             `bson:"idDisciplina"`                 // ID-ul disciplinei
	ProbeEvaluare      []ProbaEvaluare    `bson:"probeEvaluare"`                // Listează toate probele de evaluare pentru această disciplină
	MaterialeCurs      []FisierPDF        `bson:"materialeCurs,omitempty"`      // Materialele de curs (fișiere PDF)
	MaterialeLaborator []FisierPDF        `bson:"materialeLaborator,omitempty"` // Materialele de laborator (fișiere PDF)
}
