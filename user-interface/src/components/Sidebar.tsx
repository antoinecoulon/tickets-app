"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import LogoutButton from "./LogoutButton";

const navItems = [
  { name: "Tickets", path: "/dashboard/tickets" },
  { name: "Messages", path: "/dashboard/messages" },
  // TODO: Ajouter des liens selon le rôle
];

export default function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="flex flex-col justify-between items-center py-2">
      <nav>
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
