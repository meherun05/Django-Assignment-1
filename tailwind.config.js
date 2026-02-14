/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templetes/**/*.html", // **/ mean every folder inside the temp folder for temp project level
    "./**/templetes/**/*.html", // this is for app level folder for other app like user,task
    "./**/*.html",

    // Project-level templates
    "./templates/**/*.html",

    // All apps' templates (user, tasks, blog, etc.)
    "./**/templates/**/*.html",

    // Optional but recommended if you use JS or HTMX attributes
    "./static/js/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
