async function checkHealth() {
  const status = document.getElementById("status");
  const checkedAt = document.getElementById("checked-at");

  try {
    const response = await fetch("/health", {
      cache: "no-store",
    });

    if (!response.ok) throw new Error("Health check failed");

    const data = await response.json();
    status.textContent = data.status === "healthy" ? "● Healthy" : "● Degraded";
    checkedAt.textContent = "Last checked: " + new Date().toLocaleTimeString();
  } catch (error) {
    status.textContent = "● Unavailable";
    status.style.color = "#fca5a5";
  }
}

checkHealth();
setInterval(checkHealth, 30000);
