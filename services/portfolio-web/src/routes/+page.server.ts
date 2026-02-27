import type { PageServerLoad } from "./$types";
import { resolveApiBase } from "$lib/config";
import type { LoaderState, ProjectCard } from "$lib/types";

export const load: PageServerLoad = async () => {
  const apiBase = resolveApiBase();

  try {
    const response = await fetch(`${apiBase}/projects`);
    if (!response.ok) {
      throw new Error(`catalog request failed with status ${response.status}`);
    }

    const projects = (await response.json()) as ProjectCard[];
    const state: LoaderState = {
      projects,
      errorMessage: null
    };

    return state;
  } catch (error) {
    const message = error instanceof Error ? error.message : "unknown error";

    const state: LoaderState = {
      projects: [],
      errorMessage: `Unable to load project catalog: ${message}`
    };

    return state;
  }
};
