/**
 * Add your config changes here.
 * @module config
 * @example
 * export default function applyConfig(config) {
 *   config.settings = {
 *     ...config.settings,
 *     port: 4300,
 *     listBlockTypes: {
 *       ...config.settings.listBlockTypes,
 *       'my-list-item',
 *    }
 * }
 */

import SocialSharing from '@codesyntax/volto-social-sharing/SocialSharing';
import { DEFAULT_SOCIAL } from '@codesyntax/volto-social-sharing/defaultSettings';

// All your imports required for the config here BEFORE this line
import '@plone/volto/config';

// Push new item
DEFAULT_SOCIAL.push(
  // {
  //   name: 'Twitter',
  //   fa_name: ['fab', 'twitter'],
  //   color: '#00acee', //#1da1f2
  //   sharing_url: 'https://twitter.com/intent/tweet?url=',
  //   id: 'tw',
  // },
  {
    name: 'Linkedin',
    fa_name: ['fab', 'linkedin'],
    color: '#0e76a8',
    sharing_url: 'https://www.linkedin.com/sharing/share-offsite/?url=',
    id: 'li',
  },
  {
    name: 'Telegram',
    fa_name: ['fab', 'telegram'],
    color: '#229ED9',
    sharing_url: 'https://telegram.me/share/url?url=',
    id: 'tg_d',
    only_mobile: false,
  },
  {
    name: 'Whatsapp',
    fa_name: ['fab', 'whatsapp'],
    color: '#128c7e',
    sharing_url: 'https://wa.me/?text=',
    id: 'wa_d',
    only_mobile: false,
  },
);

export default function applyConfig(config) {
  config.settings = {
    ...config.settings,
    isMultilingual: false,
    supportedLanguages: ['es'],
    defaultLanguage: 'es',
    socialNetworks: [
      {
        id: 'facebook',
        href: 'https://facebook.com/groups/1606992572809602/',
        // title: 'Connect on Facebook Group',
      },
      {
        id: 'linkedin',
        href: 'https://www.linkedin.com/company/scrum-latam-comunidad/',
        // title: 'Connect on Linkedin',
      },
      {
        id: 'youtube',
        href: 'https://www.youtube.com/@ScrumLatamComunidad',
        // title: 'Watch on Youtube',
      },
      {
        id: 'telegram',
        href: 'https://t.me/+LXuWe0Rd69FjZTBh',
        // title: 'Connect on Telegram',
      },
      {
        id: 'discord',
        href: 'https://discord.gg/C72wDDHU',
        // title: 'Connect on Discord',
      },
      {
        id: 'instagram',
        href: 'https://www.instagram.com/scrumlatamcomunidad/',
        // title: 'Connect on Instagram',
      },
      {
        id: 'twitter',
        href: 'https://twitter.com/latam_scrum',
        // title: 'Connect on Twitter',
      },
      {
        id: 'whatsapp',
        href: 'https://web.whatsapp.com/send?phone=+57%20324%206834342',
        // title: 'Connect on WhatsApp',
      },
    ],
    appExtras: [
      ...config.settings.appExtras,
      {
        match: '',
        component: SocialSharing,
        props: {
          socialElements: DEFAULT_SOCIAL,
        },
      },
    ],
  };
  return config;
}
