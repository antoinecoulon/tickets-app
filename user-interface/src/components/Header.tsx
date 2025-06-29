export default function Header() {
  return (
    <header className="h-16 bg-white border-b shadow-sm flex items-center px-6 justify-between">
      <div className="text-lg font-semibold">Tableau de bord</div>
      {/* On affichera ici le rôle / nom de l'utilisateur via Zustand plus tard */}
    </header>
  );
}
