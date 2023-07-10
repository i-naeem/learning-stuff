import './index.css';
import React from 'react';
import Root, { loader as rootLoader, action as rootAction } from './routes/root.jsx';
import ReactDOM from 'react-dom/client';
import ErrorPage from './error-page.jsx';
import Contact, { loader as contactLoader } from './routes/contact';
import EditContact, { action as editAction } from './routes/edit';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import { action as destroyAction } from './routes/destroy';

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
        action: editAction,
        loader: contactLoader,
        element: <EditContact />,
        path: '/contacts/:contactId/edit',
      },
      {
        path: 'contacts/:contactId/destroy',
        action: destroyAction,
        errorElement: <div>Oh No there was an error try again.</div>,
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
);
