import { Ticket } from "@/types/Ticket";
import {
  ColumnDef,
  flexRender,
  getCoreRowModel,
  useReactTable,
} from "@tanstack/react-table";
import { useMemo } from "react";
import dayjs from "dayjs";
import "dayjs/locale/fr"
dayjs.locale("fr")

type Props = {
  data: Ticket[];
};

export default function TicketsTable({ data }: Props) {
  const columns = useMemo<ColumnDef<Ticket>[]>(
    () => [
      {
        accessorKey: "id",
        header: "ID",
      },
      {
        accessorKey: "titre",
        header: "Titre",
      },
      {
        accessorKey: "description",
        header: "Description",
      },
      {
        accessorKey: "statut",
        header: "Statut",
      },
      {
        accessorKey: "priorite",
        header: "Priorité",
      },
      {
        accessorKey: "createdAt",
        header: "Créé le",
        cell: ({ row }) => {
          const raw = row.original.createdAt
          const date = dayjs(raw)
          return date.isValid() ? date.format("DD/MM/YYYY HH:mm") : "Date invalide"
        }
      },
    ],
    []
  );

  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
  });

  return (
    <div className="rounded-md border border-gray-300 overflow-x-auto">
      <table className="min-w-full text-left text-sm">
        <thead className="bg-gray-100 text-gray-700">
          {table.getHeaderGroups().map((headerGroup) => (
            <tr key={headerGroup.id}>
              {headerGroup.headers.map((header) => (
                <th key={header.id} className="px-4 py-2 font-semibold">
                  {flexRender(
                    header.column.columnDef.header,
                    header.getContext()
                  )}
                </th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody className="divide-y divide-gray-200">
          {table.getRowModel().rows.map((row) => (
            <tr key={row.id} className="hover:bg-gray-50">
              {row.getVisibleCells().map((cell) => (
                <td key={cell.id} className="px-4 py-2">
                  {flexRender(cell.column.columnDef.cell, cell.getContext())}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
