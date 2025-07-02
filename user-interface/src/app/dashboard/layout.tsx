"use client";

import Header from "@/components/Header";
import HydrationGate from "@/components/HydrationGate";
import Sidebar from "@/components/Sidebar";
import { useUserStore } from "@/store/userStore";
import { useRouter } from "next/navigation";
import React, { useEffect, useState } from "react";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const router = useRouter()
  const token = useUserStore((state) => state.token)

  const [checked, setChecked] = useState(false)

  useEffect(() => {
    // Evite le 'flicker' du premier render (on ne sait pas encore si user logged)
    if (token === null) {
      setChecked(true)
    } else if (token) {
      setChecked(true)
    }
  }, [token])

  useEffect(() => {    
    if (checked && token === null) {
      router.push("/login")
    } else {
      setChecked(true)  
    }
  }, [checked, token])

  if (!checked) {
    return (
      <div className="h-screen w-screen flex items-center justify-center">
        <span className="text-gray-600">Chargement...</span>  {/* TODO: loader */}
      </div>
    );
  }
  
  return (
    <HydrationGate>
      <div className="flex h-screen bg-gray-100 text-gray-900">
        <Sidebar />
        <div className="flex flex-col flex-1">
          <Header />
          <main className="flex-1 overflow-y-auto p-6">{children}</main>
        </div>
      </div>
    </HydrationGate>
  );
}
