package configs

import (
	"os"
)

func EnvMongoURI() string {
	return os.Getenv("ME_CONFIG_MONGODB_URL")
}
