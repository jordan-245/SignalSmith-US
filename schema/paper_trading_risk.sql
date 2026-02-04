-- Paper trading risk metadata (Hougaard-inspired).
-- Adds flexible JSON fields for stop/risk/time-stop metadata.

alter table if exists public.paper_orders
  add column if not exists rules_json jsonb;

alter table if exists public.paper_positions
  add column if not exists rules_json jsonb;
