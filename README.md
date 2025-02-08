# Number Classification API

This API classifies numbers and returns interesting mathematical properties along with a fun fact.

## Description

This API accepts a number as input and provides information about its properties, including whether it's an Armstrong number, and whether it's even or odd. It also includes the sum of the digits and a fun fact about the number retrieved from the Numbers API.

## API Endpoint

GET /api/classify-number?number=<number>

## Request Parameters

*   number (required): An integer.

## Response Format (JSON)

200 OK:

`json
{
  "number": 371,
  "is_prime": false,  // (Will be true/false if implemented)
  "is_perfect": false, // (Will be true/false if implemented)
  "properties": ["armstrong", "odd"], // Or ["armstrong", "even"], ["odd"], ["even"]
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}