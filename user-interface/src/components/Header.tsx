"use client"

import { useUserStore } from "@/store/userStore";
import dayjs from "dayjs";

export default function Header() {
  const username = useUserStore((state) => state.username)
  
  const greetings = () => {
    const now = dayjs()
    const hour = now.hour()
    console.log('rendering')

    if (hour > 7) {
      return `Bonjour, ${username} !`
    } else if (hour > 18) {
      return `Bonsoir, ${username} !`
    }
  }
  
  return (
    <header className="h-16 bg-white border-b shadow-sm flex items-center px-6 justify-between">
      <div className="text-lg font-semibold">Tableau de bord</div>
      <div>{greetings()}</div>
    </header>
  );
}
