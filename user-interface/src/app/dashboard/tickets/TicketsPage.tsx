"use client";

import api from "@/lib/axios";
import { Ticket } from "@/types/Ticket";
import { useEffect, useState } from "react";
import TicketsTable from "./TicketsTable";
import Link from "next/link";

export default function TicketPage() {
  const [tickets, setTickets] = useState<Ticket[]>([])
  const [page, setPage] = useState(1)
  const [totalPages, setTotalPages] = useState(1)
  const [loading, setLoading] = useState<boolean>(true)

  useEffect(() => {
    const fetchTickets = async () => {
      try {
        const { data } = await api.get(`/tickets/?page=${page}`)
        setTickets(data.results)
        setTotalPages(Math.ceil(data.count / 10))
      } catch (err: any) {
        console.error("Erreur tickets:", err)
      } finally {
        setLoading(false)
      }
    }

    fetchTickets()
  }, [page])

  if (loading) return <div>Chargement des tickets...</div> // TODO: loader
  
  return (
    <div className="p-4">
      <h1 className="text-xl font-semibold mb-4">Liste des tickets</h1>
      <Link href={"/dashboard/tickets/create"}>
        <button
          className="p-4 mb-2 bg-blue-600 text-white py-2 rounded hover:bg-blue-700 hover:cursor-pointer"
        >Nouveau ticket</button>
      </Link>
      <TicketsTable data={tickets} />
      <div className="flex justify-around gap-2 mt-4">
        <button
          disabled={page === 1}
          onClick={() => setPage(p => p - 1)}
          className="bg-gray-200 px-2 rounded"
        >
          Précédent
        </button>
        <span>Page {page} / {totalPages}</span>
        <button
          disabled={page === totalPages}
          onClick={() => setPage(p => p + 1)}
          className="bg-gray-200 px-2 rounded"
        >
          Suivant
        </button>
      </div>
    </div>
  );
}
