module.exports = {
  title: 'spaCyTextBlob',
  tagline: 'Easy sentiment analysis for spaCy using TextBlob. Now supports spaCy 3.0!',
  url: 'https://spacytextblob.netlify.app',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  favicon: 'img/favicon.png',
  organizationName: 'SamEdwardes', // Usually your GitHub org/user name.
  projectName: 'spaCyTextBlob', // Usually your repo name.
  themeConfig: {
    prism: {
      theme: require('prism-react-renderer/themes/github'),
    },
    navbar: {
      title: 'spaCyTextBlob',
      logo: {
        alt: 'My Site Logo',
        src: 'img/favicon-250x250.png',
      },
      items: [
        {
          to: 'docs/',
          activeBasePath: 'docs',
          label: 'Docs',
          position: 'left',
        },
        {to: 'blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/samedwardes/spacytextblob',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Getting Started',
              to: 'docs/',
            },
            {
              label: 'API Reference',
              to: 'docs/api',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: 'blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/samedwardes/spacytextblob',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Sam Edwardes. Built with Docusaurus.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl:
            'https://github.com/samedwardes/spacytextblob/edit/main/website/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/samedwardes/spacytextblob/edit/main/website/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
