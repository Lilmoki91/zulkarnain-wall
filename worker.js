// worker.js
// Tembok Zulkarnain — Niflheim Protocol
// Worker: zulkarnain-wall.khairuldinsuyitno.workers.dev

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Periksa token
    const cookies = Object.fromEntries(
      (request.headers.get('Cookie') || '').split('; ').map(c => c.split('='))
    );
    const userToken = cookies['zulkarnain_stasis_token'];
    const validToken = env.STASIS_UNLOCK_TOKEN;

    if (userToken && userToken === validToken) {
      // Token SAH. Hantar index.html dari Pages.
      let originUrl = new URL(url.pathname, 'https://zulkarnain-wall.pages.dev');
      return fetch(originUrl.toString());
    }

    // Token TIDAK SAH atau TIADA. Bunuh browser sepenuhnya.
    return new Response('', {
      status: 403,
      statusText: 'Forbidden',
      headers: { 'Content-Type': 'text/plain' }
    });
  }
};
