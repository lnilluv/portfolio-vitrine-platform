export type ProjectCard = {
  slug: string;
  title: string;
  runtime_mode: string;
  stack: string[];
  skills: string[];
  business_problem: string;
  live_url: string;
  repo_url: string;
};

export type LoaderState = {
  projects: ProjectCard[];
  errorMessage: string | null;
};
