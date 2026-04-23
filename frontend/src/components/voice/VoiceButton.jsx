import { Mic } from "lucide-react";

export default function VoiceButton({ onClick, label = "Start Voice" }) {
	return (
		<button
			type="button"
			onClick={onClick}
			className="inline-flex items-center gap-2 rounded-xl border border-cyan-300/40 bg-cyan-300/10 px-4 py-2.5 text-sm font-semibold text-cyan-100 transition hover:bg-cyan-300/20"
		>
			<Mic size={16} />
			{label}
		</button>
	);
}
