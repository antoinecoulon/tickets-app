"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const navItems = [
  { name: "Tickets", path: "/dashboard/tickets" },
  { name: "Messages", path: "/dashboard/messages" },
  // TODO: Ajouter des liens selon le rôle
];

export default function Sidebar() {
  const pathname = usePathname();

  return (
    <aside>
      <div></div>
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
    </aside>
  );
}
