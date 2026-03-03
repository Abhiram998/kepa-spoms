export const API_BASE_URL =
  import.meta.env.VITE_API_URL?.replace(/\/$/, "") ||
  "";

// Common fetch options
const fetchOptions = (options: RequestInit = {}): RequestInit => ({
  ...options,
  credentials: "include", // ✅ Ensures cookies are sent with requests
});

export async function apiGet<T>(path: string): Promise<T> {
  const res = await fetch(`${API_BASE_URL}${path}`, fetchOptions());
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

// For creating new zones
export async function apiPost<T>(path: string, body: unknown): Promise<T> {
  const res = await fetch(`${API_BASE_URL}${path}`, fetchOptions({
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  }));
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

// For updating zone limits (Edit)
export async function apiPut<T>(path: string, body: unknown): Promise<T> {
  const res = await fetch(`${API_BASE_URL}${path}`, fetchOptions({
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  }));
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

export async function apiDelete<T>(path: string): Promise<T> {
  const res = await fetch(`${API_BASE_URL}${path}`, fetchOptions({ method: "DELETE" }));
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}