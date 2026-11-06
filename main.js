async function calc() {
  const age = document.getElementById("ageInput").value;
  const result = document.getElementById("result");

  if (!age) {
    result.innerHTML = "اكتب عمرك أولاً";
    return;
  }

  result.innerHTML = "جاري الحساب...";

  try {
    const res = await fetch("/api/calculate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ age: Number(age) })
    });

    const data = await res.json();

    if (data.error) {
      result.innerHTML = data.error;
      return;
    }

    result.innerHTML = `
      <b>${data.message}</b><br>
      بالأيام: ${data.days}<br>
      بالساعات: ${data.hours}<br>
      بالدقائق: ${data.minutes}
    `;
  } catch (e) {
    result.innerHTML = "صار خطأ بالسيرفر";
  }
}