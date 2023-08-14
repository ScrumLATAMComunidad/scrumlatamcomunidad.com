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
  //   id: 'pt',
  // },
  {
    name: 'Linkedin',
    fa_name: ['fab', 'linkedin'],
    color: '#0e76a8',
    sharing_url: 'https://www.linkedin.com/sharing/share-offsite/?url=',
    id: 'pt',
  },
  {
    name: 'Whatsapp',
    fa_name: ['fab', 'whatsapp'],
    color: '#128c7e',
    sharing_url: 'https://wa.me/?text=',
    id: 'pt',
  },
  {
    name: 'Telegram',
    fa_name: ['fab', 'telegram'],
    color: '#229ED9',
    sharing_url: 'https://telegram.me/share/url?url=',
    id: 'pt',
  },
);

export default function applyConfig(config) {
  config.settings = {
    ...config.settings,
    isMultilingual: false,
    supportedLanguages: ['es'],
    defaultLanguage: 'es',
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
