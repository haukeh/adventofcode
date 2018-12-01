package util

import (
	"bufio"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func ReadStringPerLine(file string) []string {
	f, err := os.Open(file)
	check(err)
	defer f.Close()
	scanner := bufio.NewScanner(f)

	var rows []string
	for scanner.Scan() {
		rows = append(rows, scanner.Text())
	}

	return rows
}
