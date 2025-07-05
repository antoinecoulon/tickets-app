"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import LogoutButton from "./LogoutButton";
import { useUserStore } from "@/store/userStore";
import { useEffect, useState } from "react";

type NavItems = {
  name: string;
  path: string;
};
// TODO: Ajouter des liens selon le rôle
// admin: tickets, messages, users (client + agent), entreprises
  // flex colonne ^
// client: mes tickets, mon entreprise
// agent: tickets (de mon entreprise), mon entreprise

export default function Sidebar() {
  const pathname = usePathname();
  const userRole = useUserStore((state) => state.role);
  const [navItems, setNavItems] = useState<NavItems[]>([]);

  useEffect(() => {
    if (userRole === "admin") {
      setNavItems([
        { name: "Tickets", path: "/dashboard/tickets" },
        { name: "Messages", path: "/dashboard/admin/messages" },
        { name: "Utilisateurs", path: "/dashboard/admin/utilisateurs" },
        { name: "Entreprises", path: "/dashboard/admin/entreprises" },
      ]);
    } else {
      setNavItems([
        { name: "Tickets", path: "/dashboard/tickets" },
        { name: "Entreprise", path: "/dashboard/entreprises" },
      ]);
    }
  }, [userRole]);

  return (
    <aside className="flex flex-col justify-between items-center py-2">
      <h1 className="font-bold">Tickets App</h1>
      <nav className="flex flex-col">
        {navItems.map((item) => (
          <Link
            key={item.path}
            href={item.path}
            className={`px-3 py-2 rounded hover:bg-gray-100 ${
              pathname.startsWith(item.path) ? "bg-gray-200 font-medium" : ""
            }`}
          >
            {item.name}
          </Link>
        ))}
      </nav>
      <LogoutButton />
    </aside>
  );
}
