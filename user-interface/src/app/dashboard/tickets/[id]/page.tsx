"use client";

import api from "@/lib/axios";
import { Ticket } from "@/types/Ticket";
import { useParams, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import dayjs from "dayjs";
import Link from "next/link";
import { Message } from "@/types/Message";
import Messages from "./Messages";

export default function TicketDetailsPage() {
  const router = useRouter();
  const { id } = useParams();
  const [ticket, setTicket] = useState<Ticket | null>(null);
  const [messages, setMessages] = useState<Message[]>([])
  const [isLoading, setIsLoading] = useState<boolean>(true);

  useEffect(() => {
    const fetchTicket = async () => {
      try {
        const response = await api.get(`/tickets/${id}/`);
        setTicket(response.data);
      } catch (err: any) {
        console.error("Erreur lors du chargement du ticket :", err);
        router.push("/dashboard/tickets/");
      } finally {
        setIsLoading(false);
      }
    };

    fetchTicket();
  }, [id]);

  useEffect(() => {
    const fetchMessages = async () => {
      try {
        const response = await api.get(`/tickets/${id}/messages/`)
        setMessages(response.data.results)
      } catch (err) {
        console.error("Erreur lors du chargement des messages: ", err)
      }
    }

    fetchMessages()
  }, [id])

  if (isLoading) return <div>Chargement en cours...</div>; // TODO: loader

  if (!ticket) return <div>Ticket introuvable</div>;

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Détail du ticket</h1>

      <div className="bg-white rounded-lg shadow p-4 space-y-2">
        <p>
          <strong>Titre :</strong> {ticket.titre}
        </p>
        <p>
          <strong>Description :</strong> {ticket.description}
        </p>
        <p>
          <strong>Statut :</strong> {ticket.statut}
        </p>
        <p>
          <strong>Priorité :</strong> {ticket.priorite}
        </p>
          <p><strong>Client :</strong> {ticket.client.username}</p>
          <p><strong>Agent :</strong> {ticket.agent?.username ?? "Non assigné"}</p>
        <p>
          <strong>Créé le :</strong>{" "}
          {dayjs(ticket.createdAt).format("DD/MM/YYYY à HH:MM")}
        </p>

        <div className="mt-6">
          <Link
            href={`/dashboard/tickets/${id}/edit`}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Modifier ce ticket
          </Link>
        </div>
      </div>
        
          <Messages 
            messages={messages}
            setMessages={setMessages}
            id={Number(id)}
          />
          
          
          </div>
  );
}
