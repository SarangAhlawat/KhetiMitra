export default function Footer() {
	return (
		<footer className="mt-12 border-t border-white/10 bg-[#040b13]">
			<div className="mx-auto grid max-w-6xl gap-6 px-4 py-8 text-sm md:grid-cols-3 md:px-8">
				<div>
					<p className="text-base font-semibold text-slate-100">KhetiMitra</p>
					<p className="mt-2 text-slate-400">AI-powered decision support for sustainable farming with explainable recommendations.</p>
				</div>
				<div>
					<p className="font-semibold text-slate-200">Farmer Tools</p>
					<ul className="mt-2 space-y-1 text-slate-400">
						<li>Crop recommendation</li>
						<li>Sustainability scoring</li>
						<li>Voice + chat advisory</li>
					</ul>
				</div>
				<div>
					<p className="font-semibold text-slate-200">Built For Impact</p>
					<p className="mt-2 text-slate-400">Transparent AI, practical guidance, and mobile-ready support for daily farmer decisions.</p>
				</div>
			</div>
			<div className="border-t border-white/10 px-4 py-3 text-center text-xs text-slate-500 md:px-8">
				KhetiMitra - AI-Powered Decision Support System for Sustainable Farming Practices
			</div>
		</footer>
	);
}
