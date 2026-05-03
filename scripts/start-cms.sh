#!/bin/bash
# Starts the local CMS editing environment.
# Run this before opening http://localhost:8000/admin/

npx decap-server &
DECAP_PID=$!

python -m http.server 8000 --directory docs &
HTTP_PID=$!

echo ""
echo "CMS ready at http://localhost:8000/admin/"
echo "Press Ctrl+C to stop both servers."
echo ""

trap "kill $DECAP_PID $HTTP_PID 2>/dev/null; echo 'Servers stopped.'" EXIT
wait
