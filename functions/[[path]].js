// functions/[[path]].js
// Tembok Zulkarnain — Niflheim Protocol (Pages Functions)

export async function onRequest(context) {
  const { request, env } = context;
  
  // Jika env tidak wujud (tiada Secret), TERUS menyekat akses
  if (!env || !env.STASIS_UNLOCK_TOKEN) {
    return new Response('', {
      status: 403,
      statusText: 'Forbidden',
      headers: { 'Content-Type': 'text/plain' }
    });
  }

  // Periksa kuki
  const cookies = Object.fromEntries(
    (request.headers.get('Cookie') || '').split('; ').map(c => c.split('='))
  );
  const userToken = cookies['zulkarnain_stasis_token'];
  const validToken = env.STASIS_UNLOCK_TOKEN;

  if (userToken && userToken === validToken) {
    // Token SAH — teruskan ke halaman asal
    return context.next();
  }

  // Token TIDAK SAH atau TIADA — bunuh browser
  return new Response('', {
    status: 403,
    statusText: 'Forbidden',
    headers: { 'Content-Type': 'text/plain' }
  });
}
