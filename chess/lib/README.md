# Chess Library

This holds game related files supplied to both server and client during their functioning.
Having these in one central place allows us to make sure we're making non-breaking changes by testing code interaction
within the efficient unit test domain, and not in API integration. API integration must also happen, but it's not of
concern to what happens in this library and should rather be handled by it's respective packages.
