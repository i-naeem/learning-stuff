import { redirect } from 'react-router-dom';
import { deleteContact } from '../contact';

export async function action({ params }) {
  if (Math.random() < 0.2) {
    throw new Error('Oh No!');
  }
  await deleteContact(params.contactId);
  return redirect('/');
}
