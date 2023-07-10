import './index.css';
import React from 'react';
import Root, { loader as rootLoader, action as rootAction } from './routes/root.jsx';
import ReactDOM from 'react-dom/client';
import ErrorPage from './error-page.jsx';
import Contact, { loader as contactLoader } from './routes/contact';
import EditContact, { action as editAction } from './routes/edit';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />,
    loader: rootLoader,
    action: rootAction,
    errorElement: <ErrorPage />,
    children: [
      { path: '/contacts/:contactId', loader: contactLoader, element: <Contact /> },
      {
        path: '/contacts/:contactId/edit',
        action: editAction,
        loader: contactLoader,
        element: <EditContact />,
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
);
