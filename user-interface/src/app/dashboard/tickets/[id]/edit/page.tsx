"use client"

import api from "@/lib/axios";
import { useUserStore } from "@/store/userStore";
import { Ticket } from "@/types/Ticket";
import { User } from "@/types/User";
import { useParams, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { useForm } from "react-hook-form";

export default function EditTicketPage() {
  const router = useRouter()
  const { register, handleSubmit, setValue, formState: { errors } } = useForm<Partial<Ticket>>()
    const { id } = useParams()
    const userRole = useUserStore((state) => state.role)

    const [isLoading, setIsLoading] = useState<boolean>(true)
    const [agents, setAgents] = useState<{id: number, username: string}[]>([])

    useEffect(() => {
        const fetchTicket = async () => {
            try {
                const response = await api.get(`/tickets/${id}/`)
                const ticket = response.data
                setValue("titre", ticket.titre)
                setValue("description", ticket.description)
                setValue("priorite", ticket.priorite)
                setValue("statut", ticket.statut)
                setValue("agent_id", ticket.agent?.id ?? "")
            } catch (err: any) {
                console.error("Erreur lors du chargement du ticket: ", err)
                router.push("/dashboard/tickets")
            } finally {
                setIsLoading(false)
            }
        }

        fetchTicket()
    }, [id, setValue, router])

    useEffect(() => {
      if (userRole === "admin" || userRole === "agent") {
        api.get("/auth/agents/").then((response) => {
          setAgents(response.data)
        })
      }
    }, [])

    const onSubmit = async (data: Partial<Ticket>) => {
        try {
            await api.patch(`/tickets/${id}/`, data)
            router.push(`/dashboard/tickets/${id}`)
        } catch (err: any) {
            console.error("Erreur lors de la mise à jour du ticket: ", err)
        }
    }

    if (isLoading) return <div>Chargement...</div> // TODO loader

    return (
        <div className="p-6 max-w-xl">
      <h1 className="text-2xl font-semibold mb-4">Modifier le ticket</h1>

      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
        <div>
          <label className="block font-medium">Titre</label>
          <input {...register("titre", { required: true })} className="input" />
          {errors.titre && <span className="text-red-500">Titre requis</span>}
        </div>

        <div>
          <label className="block font-medium">Description</label>
          <textarea {...register("description", { required: true })} className="input" />
          {errors.description && <span className="text-red-500">Description requise</span>}
        </div>

        <div>
          <label className="block font-medium">Priorité</label>
          <select {...register("priorite", { required: true })} className="input">
            <option value="basse">Basse</option>
            <option value="moyenne">Moyenne</option>
            <option value="haute">Haute</option>
          </select>
        </div>

        {["agent", "admin"].includes(userRole!) && 
        <div>
          <div>
          <label className="block font-medium">Statut</label>
          <select {...register("statut", { required: true })} className="input">
            <option value="ouvert">Ouvert</option>
            <option value="en_cours">En cours</option>
            <option value="resolu">Résolu</option>
            <option value="ferme">Fermé</option>
          </select>
          </div>
          <div>
          <label className="block font-medium">Assigner un agent</label>
          <select {...register("agent_id", { required: false })} className="input">
            <option value="">Non assigné</option>
            {agents.map((agent) => (
              <option key={agent.id} value={agent.id}>
                {agent.username}
              </option>
            ))}
          </select>
          </div>
        </div>
        }

        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Enregistrer
        </button>
      </form>
    </div>
    )
}