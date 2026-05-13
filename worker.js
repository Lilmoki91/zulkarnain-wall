// functions/worker.js
// Tembok Zulkarnain — Niflheim Protocol (Pages Functions)
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const cookies = Object.fromEntries(
      (request.headers.get('Cookie') || '').split('; ').map(c => c.split('='))
    );
    const userToken = cookies['zulkarnain_stasis_token'];
    const validToken = env.STASIS_UNLOCK_TOKEN;

    if (userToken && userToken === validToken) {
      return env.ASSETS.fetch(request);
    }

    return new Response('', {
      status: 403,
      statusText: 'Forbidden',
      headers: { 'Content-Type': 'text/plain' }
    });
  }
};
