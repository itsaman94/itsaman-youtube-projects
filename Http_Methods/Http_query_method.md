# The HTTP `QUERY` Method

The `QUERY` method is a **safe** and **idempotent** HTTP method designed for
sending complex, structured search requests. It combines the strengths of `GET`
(safe, cacheable, idempotent) with the ability to carry a **request body**
(like `POST`), making it ideal for rich search and filtering APIs.

> ℹ️ `QUERY` is defined in an IETF draft as a new HTTP method. Support may vary
> across servers, proxies, and clients, so verify compatibility before relying
> on it in production.

---

## Why use `QUERY`?

| Feature                     | `GET` | `POST` | `QUERY` |
| --------------------------- | :---: | :----: | :-----: |
| Safe (no side effects)      |   ✅   |   ❌    |    ✅    |
| Idempotent                  |   ✅   |   ❌    |    ✅    |
| Supports a request body     |   ❌   |   ✅    |    ✅    |
| Ideal for structured search |   ❌   |   ⚠️   |    ✅    |

**Key points**

- Uses a request body (unlike `GET`), so long or complex filters aren't crammed into the URL.
- Still **safe** and **idempotent** — repeating the request has no side effects.
- Ideal for complex, structured queries (nested filters, sorting, pagination).

---

## 1. Basic HTTP Example

```http
QUERY /products/search HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
  "filters": {
    "category": "laptop",
    "price": { "lt": 2000 }
  },
  "sort": ["price", "asc"],
  "limit": 20
}
```

---

## 2. `curl` Example

```bash
curl -X QUERY https://api.example.com/products/search \
  -H "Content-Type: application/json" \
  -d '{
    "filters": {
      "category": "laptop",
      "price": { "lt": 2000 }
    },
    "sort": ["price", "asc"],
    "limit": 20
  }'
```

---

## 3. JavaScript (Fetch API)

```javascript
const response = await fetch("https://api.example.com/products/search", {
  method: "QUERY",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    filters: {
      category: "laptop",
      price: { lt: 2000 },
    },
    sort: ["price", "asc"],
    limit: 20,
  }),
});

const data = await response.json();
console.log(data);
```

---

## Summary

The `QUERY` method gives you a clean, standards-friendly way to perform
**structured searches** without abusing `GET` (URL length limits) or `POST`
(loss of safety and idempotency). Reach for it when your search payload is too
complex for query-string parameters.
