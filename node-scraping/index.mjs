import fetch from 'node-fetch';
import jsdom from 'jsdom';

const { JSDOM } = jsdom;

(async () => {
    const res = await fetch('https://www.jma.go.jp/jp/week/319.html');
    const html = await res.text();
    const dom = new JSDOM(html);
    const document = dom.window.document;
    const nodes = document.querySelectorAll('#infotablefont tr:nth-child(4) td');
    const tokyoWeathers = Array.from(nodes).map(td => td.textContent.trim());
    console.log(tokyoWeathers);
})();