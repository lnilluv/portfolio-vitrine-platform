const DEFAULT_API_BASE = "http://portfolio-api:8000";

export function resolveApiBase(): string {
  return process.env.PORTFOLIO_API_BASE ?? DEFAULT_API_BASE;
}
