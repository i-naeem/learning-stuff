import Link from 'next/link';

export default function Page() {
  return (
    <p>
      Dashboard <br />
      <Link
        href="/dashboard/customers"
        className="text-blue-500 hover:underline"
      >
        Customers
      </Link>{' '}
      <br />
      <Link
        href="/dashboard/invoices"
        className="text-blue-500 hover:underline"
      >
        Invoices
      </Link>
    </p>
  );
}
