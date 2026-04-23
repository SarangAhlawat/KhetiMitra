export default function GlassCard({ title, children, className = "", action = null }) {
  return (
    <section className={`glass-panel rounded-2xl p-5 ${className}`}>
      {(title || action) ? (
        <div className="mb-4 flex items-start justify-between gap-3">
          {title ? <h3 className="text-lg font-semibold text-slate-100">{title}</h3> : <span />}
          {action}
        </div>
      ) : null}
      {children}
    </section>
  );
}
