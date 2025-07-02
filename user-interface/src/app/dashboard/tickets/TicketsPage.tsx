"use client";

import api from "@/lib/axios";
import { Ticket } from "@/types/Ticket";
import { useEffect, useState } from "react";
import TicketsTable from "./TicketsTable";
import Link from "next/link";

export default function TicketPage() {
  const [tickets, setTickets] = useState<Ticket[]>([])
  const [loading, setLoading] = useState<boolean>(true)

  useEffect(() => {
    const fetchTickets = async () => {
      try {
        const response = await api.get("/tickets/")
        setTickets(response.data)
      } catch (err: any) {
        console.error("Erreur tickets:", err)
      } finally {
        setLoading(false)
      }
    }

    fetchTickets()
  }, [])

  if (loading) return <div>Chargement des tickets...</div> // TODO: loader
  
  return (
    <div className="p-4">
      <h1 className="text-xl font-semibold mb-4">Liste des tickets</h1>
      <TicketsTable data={tickets} />
      <Link href={"/dashboard/tickets/create"}>
        <button
          className="p-4 mt-2 bg-blue-600 text-white py-2 rounded hover:bg-blue-700 hover:cursor-pointer"
        >Nouveau ticket</button>
      </Link>
    </div>
  );
}
