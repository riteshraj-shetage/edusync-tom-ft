# Automated Notification System

This project automates the extraction and summarization of academic assignments and quizzes from dynamic web portals. It uses Playwright for browser automation and is designed to be modular, resilient, and developer-friendly.

The system enforces column sorting, captures structured data from nested tables, and generates concise summaries of open uploads, submission status, and quiz schedules. It emphasizes maintainability, testability, and lifecycle-aware DOM interaction — ideal for students, educators, and backend developers who need reliable insights from web-based academic platforms.

## Features

- Enforces descending sort on assignment columns using scoped selectors and class-based logic
- Extracts assignment metadata, quiz timings, upload status, and grading info
- Summarizes extracted data into clean, readable formats for CLI or downstream use
- Modular functions for sorting, extraction, and summarization
- Explicit waits and fallback logic to handle dynamic content and avoid stale references

## Tech Stack

- Python 3.11+
- Playwright (async)
- CLI-first design
- Minimal external dependencies

## Author

**Riteshraj**  
Independent developer and MCA student focused on scalable system design, automation, and statistics-driven workflows. Passionate about clean architecture, robust error handling, and frictionless user experience.
